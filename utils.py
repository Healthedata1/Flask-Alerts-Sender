from pathlib import Path

# validate by writing to ig examples file and then as separate step running the IG Build:
def write_out(out_path,f_name,my_file):
    p = Path(out_path) / 'test_output' / f_name
    p.write_text(my_file)

# delete ig examples file when go to home:
def clear_dir(out_path, f_name):
    try:
        p = Path(out_path) / 'test_output'/ f_name
        p.unlink()
    except TypeError:
        pass
