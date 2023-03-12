import os
root = os.getcwd()
# root = os.path.join(root, 'replies')
root = os.path.join(root, 'private-do-not-open','replies')
subfolders = [ f.path for f in os.scandir(root) if f.is_dir() ]
files = []
for subfolder in subfolders:
    if any(subfolder.endswith(suffix) for suffix in ['ipynb_checkpoints','.git','Archive']):
        continue
    # print(subfolder)
    subfiles = [f.path for f in os.scandir(subfolder)]
    files += subfiles

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
            reply = '\n\n---\n## ' + text[second_line:email_start - 1] + text[email_finish + 1:asker_finish + 1] + '\n\n\n\n\n```\n' + text[asker_finish:question_finish].strip() + '\n```\n\n' + '\n\n\n\nThe Kollel replies:\n\n\n\n' + '\n\n```\n' + my_reply.strip() + '\n```\n\n\n\n\n\n\n\n'
            replies.append(reply)
    except Exception as e:
        print(e)
        continue            
    
with open("README.md", "w") as f:
    f.write("""Selected queries and replies from 
THE DAFYOMI DISCUSSION LIST
brought to you by Kollel Iyun Hadaf of Yerushalayim
Rosh Kollel: Rabbi Mordecai Kornfeld
daf@dafyomi.co.il""")


    for reply in replies[:]:
        f.write(reply)
        # html_text = markdown.markdown(reply)
        # f.write(html_text)
