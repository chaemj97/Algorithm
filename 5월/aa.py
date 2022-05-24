new_id = 'z-+.^.'
no = new_id.maketrans('-_.~!@#$%^&*()=+[{]}:?,<>/','                          ')
print(new_id.translate(no))
print(len('-_.~!@#$%^&*()=+[{]}:?,<>/'))
