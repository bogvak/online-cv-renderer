<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">ONLINE-CV-RENDERER</h1></p>
<p align="center">
	<em>Craft Your Career Story, Instantly Online</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/bogvak/online-cv-renderer?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/bogvak/online-cv-renderer?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/bogvak/online-cv-renderer?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/bogvak/online-cv-renderer?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Overview

The online-cv-renderer is a dynamic tool that transforms JSON-based personal data into professionally formatted Markdown CVs. It offers easy customization, real-time previews, and seamless deployment options. Perfect for job seekers, professionals, and recruiters looking to create, update, and share polished resumes effortlessly across various platforms and formats.

###  Project Index
<details open>
	<summary><b><code>ONLINE-CV-RENDERER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/poetry.toml'>poetry.toml</a></b></td>
				<td>- Configures Poetry's virtual environment settings for the project<br>- Enables automatic creation of virtual environments when initializing or installing dependencies<br>- Ensures consistent and isolated development environments across different machines, promoting reproducibility and preventing conflicts between project dependencies and system-wide packages<br>- Supports efficient package management and dependency resolution within the project's ecosystem.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/public.json'>public.json</a></b></td>
				<td>- This `public.json` file serves as a central data store for personal and professional information in what appears to be a resume or portfolio project<br>- It contains structured data about an individual named Bogdan Vakulyuk, including:

1<br>- Basic personal information (name, email, birthday, citizenship)
2<br>- Social media and professional profiles
3<br>- Work permits and citizenship status
4<br>- Professional skills with categorization and proficiency levels

The file is likely used to populate various sections of a personal website or online resume<br>- Its JSON format makes it easily consumable by JavaScript-based applications, allowing for dynamic rendering of the information across different parts of the site or application.

In the context of the project's architecture, this file acts as a single source of truth for the individual's data<br>- By centralizing this information in a JSON file, it becomes simple to update and maintain the content without needing to modify multiple areas of the codebase<br>- This approach also facilitates easy localization or customization of the resume/portfolio for different audiences or purposes.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>- Defines project configuration and dependencies for the Markdown CV application using Poetry<br>- Specifies Python 3.10 as the required version and includes FastAPI and Uvicorn as key dependencies<br>- Sets up the project structure, including package information and build system requirements<br>- Facilitates consistent development environment setup and streamlines dependency management for the Markdown CV project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/Taskfile.yml'>Taskfile.yml</a></b></td>
				<td>- Taskfile.yml defines project tasks for development, deployment, and preview generation<br>- It includes commands for running the server locally and remotely, deploying CV data and application files, and generating preview markdown<br>- The file sets environment variables for different scenarios and utilizes Poetry for dependency management<br>- Tasks are organized to facilitate efficient development workflows and streamline deployment processes for the CV application.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/src\gen_md.py'>gen_md.py</a></b></td>
				<td>- Generates a Markdown-formatted CV from JSON data<br>- Implements a CVGenerator class that processes various sections like personal information, skills, work experience, education, and languages<br>- Utilizes icons for visual enhancement and offers customization options<br>- Provides methods to create structured content for each CV section, ensuring a consistent and professional layout<br>- Outputs the final CV as a Markdown file for easy viewing and sharing.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/bogvak/online-cv-renderer/blob/master/src\server.py'>server.py</a></b></td>
				<td>- Serves as the main entry point for the FastAPI application, handling routing and request processing<br>- Configures static file serving, defines endpoints for the index page and CV generation, and manages environment-specific settings<br>- Integrates with the CVGenerator to produce and return the Markdown-formatted CV based on user requests and environmental conditions.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---


## Example
Generated Bogdan Vakuliuk CV: [link](bogvcv.md)