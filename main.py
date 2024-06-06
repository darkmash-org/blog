import os
# Function to create and write a file
def generate_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
# Function to read all files in the content directory
def main():
    content_dir = 'content'
    content = ""
    for file_name in os.listdir(content_dir):
        with open(os.path.join(content_dir, file_name), 'r') as file:
            content += f"""
            <div class="col-md-4">
                <div class="card">
                    <img src="template/assets/img/post-bg.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{file_name.split('.')[0]}</h5>
                        <a href="/post/{file_name.split('.')[0]}" class="btn btn-primary w-full">Open</a>
                    </div>
                </div>
            </div>
            """
    #print(content)

    page_content = ""
    with open('template/index.html', 'r') as file:
        page_content = file.read()
    page_content = page_content.replace('<!--Post-content-->', content)
    #print(page_content)
    #print(page_content)
    generate_file("index.html", page_content)
    print('Success')



main()


