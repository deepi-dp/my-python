import platform
import types

print(platform.system())

print(dir(platform))

for i in dir(platform):
    obj = getattr(platform, i)
    if isinstance(obj, types.FunctionType):
        try:
            print(i, obj())
        except:
            pass
