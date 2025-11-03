import random
import matplotlib.pyplot as plt

def generate_color():
    """Generate a random HEX color code."""
    return "#{:06x}".upper().format(random.randint(0, 0xFFFFFF))

def generate_palette(n=5):
    """Generate a palette with n random colors."""
    return [generate_color() for _ in range(n)]

def show_palette(colors):
    """Display the color palette using matplotlib."""
    plt.figure(figsize=(10, 2))
    plt.title("🎨 Random Color Palette", fontsize=16, pad=20)
    plt.axis('off')

    for i, color in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=color)
        plt.text(i + 0.5, -0.1, color, ha='center', va='top', fontsize=12)

    plt.xlim(0, len(colors))
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

def save_palette(colors, filename="palette.png"):
    """Save the palette as an image."""
    fig, ax = plt.subplots(figsize=(10, 2))
    for i, color in enumerate(colors):
        ax.fill_between([i, i + 1], 0, 1, color=color)
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"✅ Palette saved as {filename}")

if __name__ == "__main__":
    colors = generate_palette(5)
    print("🎨 Your Random Color Palette:")
    for color in colors:
        print(color)
    show_palette(colors)
    save_palette(colors)
