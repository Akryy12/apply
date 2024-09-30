import subprocess

def apply_spicetify():
    try:
        # Run the 'spicetify apply' command
        subprocess.run(["spicetify", "apply"], check=True)
        print("Spicetify applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    apply_spicetify()
