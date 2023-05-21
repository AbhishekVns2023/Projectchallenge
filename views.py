from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("Mcq-Quiz")


def answer(request):
    questions = [("(Q1)- What is the output for −'python ' [-3]?", "P", "o", "h", "t", 'c'),
                 (
                     "(Q2) - Name the python module which supports regular expressions.", "regex", "re", "pyre",
                     "pyregex", 'b'),
                 ("(Q3)Which method is used to convert raw byte data to a string?", "Encode()", "Decode()", "Convert()",
                  "tostring()", 'b'),
                 ("(Q4)- What is output for − max(''please help", "s", "a blank space character", "e", "p", 'c'),
                 ("(Q5)-What is a correct syntax to output -Hello World- in Python?", "p(hello world)",
                  "pf(hello world)",
                  "print(hello world)", "printf(hello world)")
                 ]
    x = 0
    opta = ""
    optb = ""
    optc = ""
    optd = ""
    previousquestion = ""
    result = ""
    option = ""
    score = 0

    n = len(questions)
    if request.GET:
        x = request.GET["question"]
        option = (request.GET["option"])
        score = request.GET["score"]
        x = int(x)
        score = int(score)
        previousans = questions[x][1]
        previousquestion = questions[x][0]
        if option == previousans:
            result = "Correct your score is +1"
            score = score + 1
        else:

            result = "Wrong"
        x = x + 1
        print(result, "option=", option, "ans=", previousans, score)
        if x >= n:
            return render(request, "m.html",
                          {"score": score, "result": result})  # "-- Your Scores is  ----- " + str(score)

    question = questions[x][0]
    opta = questions[x][1]
    optb = questions[x][2]
    optc = questions[x][3]
    optd = questions[x][4]

    return render(request, "mcq.html",
                  {"qno": x, "currentquestion": question, "result": result, "previousans": previousquestion,
                   "score": score, "a": opta, "b": optb, "c": optc, "d": optd,"option":option})
