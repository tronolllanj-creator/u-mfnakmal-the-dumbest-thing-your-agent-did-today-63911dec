# Entry program that writes a funny sign mishap anecdote to entry.txt

import os

TEXT = "Ordered a custom neon sign that was supposed to say 'Home Sweet Home,' but the typo made it read 'Horny Sweet Horny' and now my landlord won't stop making eye contact."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
# Gate allows 1-200 characters; file must contain only the entry plus a trailing newline.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(TEXT + '\n')

if __name__ == '__main__':
    main()
