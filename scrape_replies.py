import os
root = os.getcwd()
root = os.path.join(root, 'replies')
subfolders = [ f.path for f in os.scandir(root) if f.is_dir() ]
files = []
for subfolder in subfolders:
    if any(subfolder.endswith(suffix) for suffix in ['ipynb_checkpoints','.git','Archive']):
        continue
    # print(subfolder)
    subfiles = [f.path for f in os.scandir(subfolder)]
    files += subfiles
my_file = files[0]
with open(my_file) as f: # Use file to refer to the file object
    text = f.read()
    text_anon = ''
    record = True
    for char in text:
        if char == '<':
            record = False
        if record:
            text_anon += char
        if char == '>':
            record = True
replies = []

for file in files:
    try:
        with open(file) as f:
            text = f.read()
            first_line = text.find('_\n') + 2
            second_line = first_line + text[first_line:].find('_\n') + 3

            title = second_line + text[second_line:].find('\n')
            asker_start = title + text[title:].find('\n') + 6
            email_start = asker_start + text[asker_start:].find('<') + 1
            email_finish = email_start + text[email_start:].find('>') + 1
            asker_finish = email_finish + text[email_finish:].find(':') + 2
            question_finish = asker_finish + text[asker_finish:].find('-----')
            reply_opener = question_finish + text[question_finish:].find('--\n') + 3
            reply_start = reply_opener + text[reply_opener:].find('lies:') + 6
            my_reply = text[reply_start:].lstrip()
            my_reply = my_reply.replace("\n", "\n\n")
            my_reply = my_reply.replace("\n\n", "\n")
            reply = '\n\n---\n## ' + text[second_line:email_start - 1] + text[email_finish + 1:asker_finish + 1] + '\n\n\n```' + text[asker_finish:question_finish] + '```' + '\n\n\n\nThe Kollel replies:\n\n\n\n' + '```\n' + my_reply + '\n```\n\n\n\n\n\n'
            replies.append(reply)
    except Exception as e:
        print(e)
        continue            
    
with open("sefer.md", "w") as f:
    for reply in replies[:50]:
        f.write(reply)