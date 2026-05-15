# DRAWINGS config
DRAWINGS = [
    {"id": "p1", "label": "Character Design", "ink": "ink1.jpg", "pencil": "pencil1.jpg"},
    {"id": "p2", "label": "Sequential Page", "ink": "ink2.jpg", "pencil": "pencil2.jpg"},
    {"id": "p3", "label": "Environment", "ink": "ink3.jpg", "pencil": "pencil3.jpg"}
]

def build_site():
    # Generate the HTML snippets for the 3 drawings
    gallery_html = ""
    for item in DRAWINGS:
        gallery_html += f"""
        <div class="process-container">
            <div class="process-image ink-layer" style="background-image: url('static/{item['ink']}');"></div>
            <div class="process-image pencil-layer" id="{item['id']}" style="background-image: url('static/{item['pencil']}'); width: 50%;"></div>
            <input type="range" min="0" max="100" value="50" class="slider" oninput="moveSlider(this.value, '{item['id']}')">
            <div class="label">{item['label']}</div>
        </div>"""

    # Read your existing portfolio.html as a template
    with open("portfolio.html", "r") as f:
        template = f.read()

    # Replace a placeholder in your HTML with the generated gallery
    final_html = template.replace("<!-- GALLERY_PLACEHOLDER -->", gallery_html)

    # Output to index.html so GitHub Pages can read it
    with open("index.html", "w") as f:
        f.write(final_html)
    print("Build complete: portfolio.html merged into index.html")

if __name__ == "__main__":
    build_site()