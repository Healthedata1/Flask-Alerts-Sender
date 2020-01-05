from pathlib import Path

# validate by writing to ig examples file and then as separate step running the IG Build:
def write_out(out_path, my_file, timestamp = None):
    p = Path(out_path) / 'test_output' /f'davinci_notification_bundle_{timestamp}.json'
    p.write_text(my_file)

# delete ig examples file when go to home:
def clear_dir(out_path):
    p = Path(out_path) / 'test_output'
    p.unlink()
