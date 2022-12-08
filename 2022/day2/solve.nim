import std/strutils

const
    oRock = "A"
    oPaper = "B"
    oScissor = "C"
    
    rock = "X"
    paper ="Y"
    scissor ="Z"

    mustlose = "X"
    mustdraw ="Y"
    mustwin ="Z"


discard """
    Own choice score:
        rock 1
        paper 2
        scissor 3

    Outcome score:
        lost 0
        draw 3
        win 6
    """


proc playerMoveScore(p:string):int =
    case p:
        of rock:
            result = 1
        of paper:
            result = 2
        of scissor:
            result = 3

proc outComeScore(o,p: string):int= 
    case o:
        of oRock:
            if p == scissor:
               result = 0
            elif p == rock:
                result = 3
            elif p == paper:
                result =6
            else:
                raise newException(OSError,"invalid player move")

        of oPaper:
            if p == scissor:
                result =6
            elif p == rock:
                result =0
            elif p == paper:
                result = 3
            else:
                raise newException(OSError,"invalid player move")

        of oScissor:
            if p == scissor:
                result=3
            elif p == rock:
                result=6
            elif p == paper:
                result=0
            else:
                raise newException(OSError,"invalid player move")


let inputFile = readFile("input.txt")

let lines = splitLines(inputFile)

var totalScore = 0
for line in lines:
    let moves = splitWhitespace(line)
    if len(moves) == 0:
        break
    let o = moves[0]
    let p = moves[1]
    totalScore = totalScore + outComeScore(o,p) + playerMoveScore(p)
    
echo "Part1 solution: " & $(totalScore)


proc getPlayerMove(o,r:string):string =
    case r:
        of mustdraw:
            case o:
                of oPaper:
                    result = paper
                of oRock:
                    result = rock
                of oScissor:
                    result = scissor
        of mustlose:
            case o:
                of oPaper:
                    result = rock
                of oScissor:
                    result = paper
                of oRock:
                    result = scissor
        of mustwin:
            case o:
                of oPaper:
                    result = scissor
                of oScissor:
                    result = rock
                of oRock:
                    result = paper

totalScore = 0
for line in lines:
    let round = splitWhitespace(line)
    if len(round) == 0:
        break
    var
        o = round[0]
        r = round[1]
        p = getPlayerMove(o,r)
    totalScore = totalScore + outComeScore(o,p) + playerMoveScore(p)

echo "Part2 solution: " & $(totalScore)
