# Short Circuiting
is_Friend = True
is_User = True

# or will stop evaluating if is_Friend is true because it will already return true
# it doesn't need to continue trying to evaluate.  This is short-circuiting.
if is_Friend or is_User:
    print('best friends forever')
