# Task 2
# Class for Parser


# 1 Packages
#-----------

import sys



# 2 Class Parser
#---------------

class Parser:
  
  
  
  
  def ImportGraph(self, filename):
    try:
      file = open(filename,'r')
    except:
      sys.stderr.write("Unable to open file " + filename + "\n")
      sys.exit()


    FirstLine = True
    Nodes = []
    Arcs = dict()
    
    
    for line in file:
      if FirstLine:
        FirstLine = False
        
        






# Test
parser = Parser()
parser.ImportGraph('ParserTesttext.txt')






# def Import_Championship(filename):
#   try:
#     file = open(filename,'r')
#   except:
#     sys.stderr.write("Unable to open file " + filename + "\n")
#     sys.exit()

#   championship = {Championship_Teams:{}, Championship_Games:{}}
#   teams = []
#   games = []
#   for line in file:
#     line = line.strip()
#     tokens = line.split('	')
#     if tokens[0] == Code_TeamsList:
#       continue
#     if tokens[0] == Code_GameList:
#       continue
#     else:
#       if len(tokens) == 2:
#         team = Parser_SetTeam(tokens)
#         teams.append(team)
#       if len(tokens) == 4:
#         game = Game.Game_New(tokens[0], int(tokens[1]),tokens[2],int(tokens[3]))
#         games.append(game)
#   championship[Championship_Games] = games
#   championship[Championship_Teams] = teams
#   return championship

