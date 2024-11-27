import os

def generate_metadata(repo_dir, output_file, base_url, architecture="x86_64"):
    metadata_entries = []

    for file in os.listdir(repo_dir):
        if file.endswith(".night"):
            try:
                name, version = file.split("-", 1)
                version = version.rsplit(".", 1)[0]
                url = f"{base_url}/{architecture}/{file}"
                metadata_entries.append(f"{name}|{version}|{architecture}|{url}")
            except ValueError:
                print(f"Skipping invalid file: {file}")
    
    with open(output_file, 'w') as f:
        f.write("\n".join(metadata_entries))

    print(f"Generated metadata.list at {output_file}")

repo_directory = "./repo"
output_metadata = "./metadata.list"
repository_base_url = "https://nightlinux.github.io/nightrepo/"
