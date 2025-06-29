import markdown
import argparse

def convert_markdown_to_html(input_file, output_file):
    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()

    # Convert to HTML using markdown with code support
    html = markdown.markdown(
        markdown_text,
        extensions=['fenced_code', 'codehilite']  # ensures ``` blocks work
    )

    # Optional: wrap in basic HTML boilerplate
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Converted Markdown</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        pre code {{ background: #f4f4f4; padding: 10px; display: block; border-radius: 5px; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
    </style>
</head>
<body>
{html}
</body>
</html>
"""

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)

    print(f"[✓] HTML file generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("input", help="Input .md file")
    parser.add_argument("output", help="Output .html file")
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)
