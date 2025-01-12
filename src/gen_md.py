import json 
import itertools
from os import getenv


class CVGenerator:

    icons = {
        "default": "envelope.png",
        "envelope": "envelope.png",
        "phone": "phone-solid.png",
        "birthday": "cake-candles-solid.png",
        "github": "github.png",
        "linkedin": "linkedin.png",
        "instagram": "instagram.png",
        "slideshare": "slideshare.png",
        "facebook": "envelope.png",
        "url": "url.png",
    }

    def __init__(self, 
                 host="https://cv.bogv.online",
                 file=getenv("CVFILE", "public.json"),
                 show_private=False):
        self.host = host
        self.show_private = show_private
        self.file = file

    def get_image(self, img_src, img_descr):
        return f"![{img_descr}]({self.host}/static/{img_src})"

    def get_icon(self, icon_name):
        icon =  self.icons.get(icon_name, self.icons['default'])
        return self.get_image(icon, icon_name)

    def get_getter(self, section):
        """
        Returns a function that generates a getter function for a given key.

        The getter function takes a dictionary as input and returns the value
        associated with the key. If the key is not found, it returns None.

        Returns:
            function: A function that generates getter functions.
        """
        def getter(path, default=None):
            """
            Retrieve a value from a nested dictionary using a dot-separated path.
            
            Args:
                path (str): The dot-separated key path (e.g., "cat.head.think").
                data (dict): The dictionary to search.
                default: The default value to return if the path is not found.
            
            Returns:
                The value from the dictionary or the default value.
            """
            keys = path.split(".")
            current = section
            try:
                for key in keys:
                    current = current[key]
                return current
            except (KeyError, TypeError):
                return default
        return getter

    def generate_basics(self, cv_json_source):
        """
        Generates a personal Markdown section from the given JSON source.

        Args:
            cv_json_source (dict): The JSON source containing personal information.

        Returns:
            str: The generated personal section as a string.
        """
        # Generate Markdown for personal section
        g = self.get_getter(cv_json_source.get('basics', {}))
        section = f" {self.get_image(g('photo'), 'my photo')} \n"
        section += f"# {g('name')} :: "
        
        # Socials
        socials = g('social', [])
        socials_string = [f"[{self.get_icon(social['network'])}]({social['url']})" for social in socials]
        section += " ".join(socials_string) + f"\n\n"
        ## Full CV Link
        section += f"{self.get_icon('url')} [Full online CV]({self.host}) "
        section += f"{self.get_icon('envelope')} [{g('email')}](mailto:{g('email')}) "
        
        # Phones
        if self.show_private:
            phones = g('phones', [])
            phones_string = [f"{self.get_icon('phone')} {phone['country']}:{phone['number']}" for phone in phones]
            section += f"{' '.join(phones_string)} "
        section += f"{self.get_icon('birthday')} {g('birthday')} \n\n"

        return section

    def generate_skills(self, cv_json_source):
        """
        Generates a skills Markdown section from the given JSON source.

        Args:
            cv_json_source (dict): The JSON source containing skills information.

        Returns:
            str: The generated skills section as a string.
        """
        # Generate Markdown for skills section
        skills_init = cv_json_source.get('skills', [])
        skills = sorted(skills_init, key=lambda x: x['level'], reverse=True)
        skills_by_type = sorted(skills_init, key=lambda x: x['type'], reverse=True)
        categories = self.get_categories_set(skills_by_type)
        section = f"## Skills (level from 0 to 9)\n\n"
        sections = []
        for category in categories:
            skills_in_category = [skill for skill in skills if category in skill['categories']]
            skill_string = [f"{skill['name']}<sup>{skill['level']}</sup>" for skill in skills_in_category]
            sections.append(f"**<mark> {category} </mark>** " + " • ".join(skill_string))
        section += "\\\n".join(sections)
        section += f" \n\n"
        return section 

    def generate_work(self, cv_json_source):
        """
        Generates a work Markdown section from the given JSON source.

        Args:
            cv_json_source (dict): The JSON source containing work information.

        Returns:
            str: The generated work section as a string.
        """
        # Generate Markdown for work section
        work = cv_json_source.get('work', [])

        section = f"## Work\n\n"
        for index, work_item in enumerate(work):
            g = self.get_getter(work_item)
            if index > 0:
                section += f"---\n\n"
            section += f"### *{g('startDate')} - {g('endDate')}* || **{g('name')}** || {g('position')}\n\n"
            # Technologies
            technologies = g('technologies', [])
            techstring = " • ".join(technologies)
            section += f"`{techstring}`\n\n"
            # section += f"{g('summary')} \n"
            resp_strings = [f"- {resp}" for resp in g('highlights')]
            section += '\n'.join(resp_strings)        
            # Projects
            projects = g('projects', [])
            if len(projects) > 0:
                section += f"#### Projects: \n\n"
            else:
                # pass
                section += f"\n\n"
            for index, project in enumerate(projects):
                if index > 0:
                    section += f"---\n\n"
                section += f"| Project | Duration | Role |\n"
                section += f"| --- | --- | --- |\n"
                section += f"| **{project['name']}** | {project['duration']} | {project['role']} |\n\n"
                technologies = project['technologies']
                techstring = " • ".join(technologies)
                section += f"`{techstring}`\n\n"
                section += f"- {project['summary']} \n\n"
                # section += '\n'.join(resp_strings)
                # section += f"\n\n"
        return section

    def generate_education(self, cv_json_source):
        """
        Generates an education Markdown section from the given JSON source.

        Args:
            cv_json_source (dict): The JSON source containing education information.

        Returns:
            str: The generated education section as a string.
        """
        # Generate Markdown for education section
        education = cv_json_source.get('education', [])

        section = f"## Education\n\n"
        for education_item in education:
            g = self.get_getter(education_item)
            section += f"**{g('institution')}**\n\n"
            section += f"{g('studyType')} \n"
            section += f"{g('endDate')} \n"
            section += f"{g('area')} \n"
            section += f"\n\n"
        return section

    def generate_languages(self, cv_json_source):
        """
        Generates a languages Markdown section from the given JSON source.

        Args:
            cv_json_source (dict): The JSON source containing language information.

        Returns:
            str: The generated languages section as a string.
        """
        # Generate Markdown for languages section
        languages = cv_json_source.get('languages', [])

        section = f"## Languages\n\n"
        lang_strings = [f"**{lang['language']}**: {lang['fluency']}" for lang in languages]
        section += " • ".join(lang_strings)
        section += f"\n\n"
        return section

    def get_categories_set(self, skills):
        """
        Retrieves a set of unique categories from the skills section of the JSON source.

        Returns:
            set: A set of unique categories.
        """
        result = []
        seen = set()

        for entry in skills:
            for category in entry["categories"]:
                unique_key = (category, entry["type"])  # Ensure unique cat-type pair
                if unique_key not in seen:
                    seen.add(unique_key)
                    result.append({"cat": category, "type": entry["type"]})

        result = sorted(result, key=lambda x: x["type"], reverse=True)
        return [entry["cat"] for entry in result]        

    def md_line(self):
        return "--- \n\n"

    def get_md_cv(self):
        cv_json_source = json.load(open(self.file, 'r'))
        doc = self.generate_basics(cv_json_source)
        doc += self.md_line()
        doc += self.generate_skills(cv_json_source)
        doc += self.md_line()
        doc += self.generate_work(cv_json_source)
        doc += self.md_line()
        doc += self.generate_education(cv_json_source)
        doc += self.md_line()
        doc += self.generate_languages(cv_json_source)
        doc += self.md_line()
        return doc

# Main entrypoint
if __name__ == '__main__':
    
    cvgen = CVGenerator(
        host=getenv("CVHOST", "https://cv.bogv.online"),
        show_private=True
        )
    doc = cvgen.get_md_cv()
    
    # save to file
    with open('preview.md', 'w', encoding="utf-8") as f:
        f.write(doc)