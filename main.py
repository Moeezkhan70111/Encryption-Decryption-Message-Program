print("Press 1 for Encryptions and 2 for Decryption:\n")
choice=int(input())

if (choice == 1):
 msg = input("Enter Your message:\n")
 newmsg = msg.lower()
 rep = newmsg.replace("a", "!")
 rep = rep.replace("b", "@")
 rep = rep.replace("c", "#")
 rep = rep.replace("d", "$")
 rep = rep.replace("e", "%")
 rep = rep.replace("f", "^")
 rep = rep.replace("g", "&")
 rep = rep.replace("h", "*")
 rep = rep.replace("i", "(")
 rep = rep.replace("j", ")")
 rep = rep.replace("k", "_")
 rep = rep.replace("l", "`")
 rep = rep.replace("m", "~")
 rep = rep.replace("n", "-")
 rep = rep.replace("o", "+")
 rep = rep.replace("p", "=")
 rep = rep.replace("q", "{")
 rep = rep.replace("r", "}")
 rep = rep.replace("s", "[")
 rep = rep.replace("t", "]")
 rep = rep.replace("u", ":")
 rep = rep.replace("v", ";")
 rep = rep.replace("w", "/")
 rep = rep.replace("x", "?")
 rep = rep.replace("y", "<")
 rep = rep.replace("z", ">")
 rep = rep.replace(" ", ".")
 print(rep)
elif(choice == 2):
   msg = input("Enter Your message:\n")
   newmsg = msg.lower()
   rep = newmsg.replace("!", "a")
   rep = rep.replace("@", "b")
   rep = rep.replace("#", "c")
   rep = rep.replace("$", "d")
   rep = rep.replace("%", "e")
   rep = rep.replace("^", "f")
   rep = rep.replace("&", "g")
   rep = rep.replace("*", "h")
   rep = rep.replace("(", "i")
   rep = rep.replace(")", "j")
   rep = rep.replace("_", "k")
   rep = rep.replace("`", "l")
   rep = rep.replace("~", "m")
   rep = rep.replace("-", "n")
   rep = rep.replace("+", "o")
   rep = rep.replace("=", "p")
   rep = rep.replace("{", "q")
   rep = rep.replace("}", "r")
   rep = rep.replace("[", "s")
   rep = rep.replace("]", "t")
   rep = rep.replace(":", "u")
   rep = rep.replace(";", "v")
   rep = rep.replace("/", "w")
   rep = rep.replace("?", "x")
   rep = rep.replace("<", "y")
   rep = rep.replace(">", "z")
   rep = rep.replace(".", " ")
   print(rep)
else:
  print("Invalid Choice")
