#!/usr/bin/env python3
"""
Generate icons for Copilot Dev Camp plugin
- color.png (192×192) - Full-color book in tent icon
- outline.png (32×32) - Outline version for use as app mask
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_color_icon():
    """Create the full-color icon (192×192)"""
    size = 192
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle - black
    bg_color = (0, 0, 0, 255)  # Black background
    draw.ellipse([10, 10, size-10, size-10], fill=bg_color)
    
    # Tent shape (triangle) - purple
    tent_color = (155, 89, 182, 255)  # Purple
    tent_points = [
        (size//2, 30),      # Top point
        (40, size-40),      # Bottom left
        (size-40, size-40)  # Bottom right
    ]
    draw.polygon(tent_points, fill=tent_color, outline=(0, 0, 0, 50))
    
    # Tent entrance line
    draw.line([(size//2, 30), (size//2, size-40)], fill=(255, 255, 255, 150), width=3)
    
    # Book - open book shape inside tent
    # Book spine
    book_x = size//2 - 12
    book_y = 70
    book_width = 24
    book_height = 60
    
    # Left page
    left_page_color = (230, 220, 200, 255)
    draw.rectangle(
        [book_x-book_width//2, book_y, book_x, book_y+book_height],
        fill=left_page_color,
        outline=(80, 60, 40, 200),
        width=1
    )
    
    # Right page
    right_page_color = (255, 250, 240, 255)
    draw.rectangle(
        [book_x, book_y, book_x+book_width//2, book_y+book_height],
        fill=right_page_color,
        outline=(80, 60, 40, 200),
        width=1
    )
    
    # Book spine
    draw.rectangle(
        [book_x-2, book_y, book_x+2, book_y+book_height],
        fill=(100, 80, 60, 255),
        outline=(60, 40, 20, 200)
    )
    
    # Add text lines on pages to represent content
    line_color = (150, 120, 100, 180)
    y_offset = book_y + 12
    for i in range(3):
        # Left page lines
        draw.line([(book_x-book_width//2+5, y_offset), (book_x-3, y_offset)], fill=line_color, width=1)
        y_offset += 12
    
    y_offset = book_y + 12
    for i in range(3):
        # Right page lines
        draw.line([(book_x+3, y_offset), (book_x+book_width//2-5, y_offset)], fill=line_color, width=1)
        y_offset += 12
    
    # Stars around for "camp" theme
    star_color = (255, 215, 0, 200)
    star_positions = [(30, 50), (size-25, 55), (35, size-35)]
    for sx, sy in star_positions:
        draw.polygon(
            [(sx, sy-4), (sx+2, sy-1), (sx+5, sy-1), (sx+3, sy+1), (sx+4, sy+4), 
             (sx, sy+2), (sx-4, sy+4), (sx-3, sy+1), (sx-5, sy-1), (sx-2, sy-1)],
            fill=star_color
        )
    
    return img

def create_outline_icon():
    """Create the outline icon (32×32) for app mask"""
    size = 32
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outline color (white for mask)
    outline_color = (255, 255, 255, 255)
    bg_color = (0, 0, 0, 255)
    
    # Background circle
    draw.ellipse([1, 1, size-1, size-1], outline=outline_color, width=2)
    
    # Simplified tent outline
    tent_points = [
        (size//2, 4),
        (6, size-6),
        (size-6, size-6)
    ]
    draw.polygon(tent_points, outline=outline_color, width=2, fill=None)
    
    # Center line for tent
    draw.line([(size//2, 4), (size//2, size-6)], fill=outline_color, width=1)
    
    # Simplified book - open book shape
    book_x = size//2
    book_y = 10
    book_h = 12
    
    # Book pages (simple rectangles)
    draw.rectangle([book_x-5, book_y, book_x-2, book_y+book_h], outline=outline_color, width=1)
    draw.rectangle([book_x+2, book_y, book_x+5, book_y+book_h], outline=outline_color, width=1)
    
    # Book spine
    draw.line([(book_x-1, book_y), (book_x+1, book_y)], fill=outline_color, width=1)
    draw.line([(book_x-1, book_y+book_h), (book_x+1, book_y+book_h)], fill=outline_color, width=1)
    
    return img

def main():
    # Get the plugin root directory
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate color icon
    print("Generating color icon (192×192)...")
    color_img = create_color_icon()
    color_path = os.path.join(plugin_dir, 'color.png')
    color_img.save(color_path, 'PNG')
    print(f"✅ Created: {color_path}")
    
    # Generate outline icon
    print("Generating outline icon (32×32)...")
    outline_img = create_outline_icon()
    outline_path = os.path.join(plugin_dir, 'outline.png')
    outline_img.save(outline_path, 'PNG')
    print(f"✅ Created: {outline_path}")
    
    print("\n✨ Icon generation complete!")
    print(f"   color.png:   {os.path.getsize(color_path)} bytes")
    print(f"   outline.png: {os.path.getsize(outline_path)} bytes")

if __name__ == '__main__':
    main()
