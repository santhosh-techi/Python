def scope():
    x='sunny'
    def get_name():
        print(x)
    get_name()
    
y=scope()
print(y)
