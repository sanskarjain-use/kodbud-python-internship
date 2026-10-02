"""Task 4: Rename files in a folder to file_1.ext, file_2.ext, ..."""
import os


def rename_files(folder, prefix="file"):
    files = sorted(f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    # Two passes so new names never collide with existing ones
    temp = []
    for i, name in enumerate(files, 1):
        ext = os.path.splitext(name)[1]
        tmp = f"__tmp_{i}{ext}"
        os.rename(os.path.join(folder, name), os.path.join(folder, tmp))
        temp.append((tmp, f"{prefix}_{i}{ext}"))
    for tmp, final in temp:
        os.rename(os.path.join(folder, tmp), os.path.join(folder, final))
        print(f"-> {final}")
    return len(files)


def main():
    folder = input("Enter folder path: ").strip()
    if not os.path.isdir(folder):
        print("Error: folder not found.")
        return
    count = rename_files(folder)
    print(f"Renamed {count} file(s).")


if __name__ == "__main__":
    main()
