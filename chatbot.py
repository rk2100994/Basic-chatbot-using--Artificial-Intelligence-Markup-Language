import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml")

# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Please enter your message ")))
