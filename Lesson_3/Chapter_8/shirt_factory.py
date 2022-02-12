#shirt_factory.py
def make_shirt(size='medium', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nYour shirt is a size " + size + " with the message '" + message + "' printed on the front")

make_shirt()
make_shirt(size='large')
make_shirt('small', 'In a world where you can be anything, be kind') 