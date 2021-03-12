import sys

# αρχικοποίηση μέτωπου αναζήτησης με το σημείο εκκίνησης:
SearchFront = [[[4, 0]]]

# σημείο τερματισμού:
FinalState = [2, 4]

#κόστος (αρχικοποίηση με την μέγιστη τιμή):
BestCost = sys.maxsize

#καλύτερη διαδρομή αλγορίθμου:
BestRoute = []

# Η διαδρομή που κάναμε μέχρι τώρα:
route = []

#καταστάσεις παιδιά:
children = []

# Μετρητής επαναλήψεων:
CounterReps = 0

#Λαβύρινθος
labyrinth = [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 0],
             [1, 0, 1, 0, 1],
             [0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

# Η συνάρτηση με την οποία βρίσκουμε τις καταστάσεις παιδιά
def children_stalker(route):
    x = y = 0
    coordinate = []
    childrenStates = []
    if len(route) == 1:
        coordinate = route[0]
        x = coordinate[1]
        y = coordinate[0]
    elif len(route) > 1:
        coordinate = route[-1]
        x = coordinate[1]
        y = coordinate[0]
    print('ΜΕΤΩΠΟ ΑΝΑΖΗΤΗΣΗΣ: '+str(SearchFront))
    print('ΤΩΡΙΝΗ ΘΕΣΗ: ' + str(coordinate))
    print('ΔΙΑΔΡΟΜΗ ΜΕΧΡΙΣ ΣΤΙΓΜΗΣ: ' + str(route))


    if len(route) < BestCost:
        print('ΘΑ ΠΑΜΕ:')

        # κινουμε βορεια
        if y - 1 >= 0:
            if labyrinth[y - 1][x] == 0:
                northChildrenX = x
                northChildrenY = y - 1
                if [y - 1, x] not in route:
                    northChildren = route + [[northChildrenY, northChildrenX]]
                    childrenStates.append(northChildren)
                    print(" ΒΟΡΕΙΑ ")

        try:
            # κινουμε ανατολικα
            if labyrinth[y][x + 1] == 0:
                eastChildrenX = x + 1
                eastChildrenY = y
                if [y, x + 1] not in route:
                    eastChildren = route + [[eastChildrenY, eastChildrenX]]
                    childrenStates.append(eastChildren)
                    print(" ΑΝΑΤΟΛΙΚΑ ")
        except IndexError:
            pass

        try:
            #κινουμε νοτια
            if labyrinth[y + 1][x] == 0:
                southChildrenX = x
                southChildrenY = y + 1
                if [y + 1, x] not in route:
                    southChildren = route + [[southChildrenY, southChildrenX]]
                    childrenStates.append(southChildren)
                    print(" ΝΟΤΙΑ ")
        except IndexError:
            pass


        # κινουμε δυτικα
        if x - 1 >= 0:
            if labyrinth[y][x - 1] == 0:
                westChildrenX = x - 1
                westChildrenY = y
                if [y, x - 1] not in route:
                    westChildren = route + [[westChildrenY, westChildrenX]]
                    childrenStates.append(westChildren)
                    print(" ΔΥΤΙΚΑ ")
        else:
            pass

    else:
        print('ΚΛΑΔΕΜΑ, ΚΑΛΥΤΕΡΟ ΚΟΣΤΟΣ: ' + str(BestCost))
    return childrenStates


while len(SearchFront) != 0:
    CounterReps += 1
    print("\nΑΡΙΘΜΟΣ ΕΠΑΝΑΛΗΨΕΩΝ: " + str(CounterReps))
    route = SearchFront[0]
    SearchFront.pop(0)
    if route[-1] != FinalState:
        children = children_stalker(route)
        SearchFront = children + SearchFront
        children.clear()
    else:
        print('Η ΔΙΑΔΡΟΜΗ ΟΛΟΚΛΗΡΩΘΗΚΕ')
        print('ΔΙΑΔΡΟΜΗ: ' + str(route))
        CurrentCost = len(route) - 1
        print('ΚΟΣΤΟΣ ΓΙΑ ΑΥΤΗΝ ΤΗΝ ΔΙΑΔΡΟΜΗ: ' + str(CurrentCost))
        if CurrentCost < BestCost:
            BestRoute = route
            BestCost = CurrentCost

if BestCost == sys.maxsize:
    print("ΚΑΤΙ ΠΗΓΕ ΣΤΡΑΒΑ")
else:
    print("\nΤΕΛΟΣ ΑΛΓΟΡΙΘΜΟΥ")
    print("ΕΛΑΧΙΣΤΟ ΚΟΣΤΟΣ " + str(BestCost) + " ΜΕ ΜΟΝΟΠΑΤΙ " + str(BestRoute) + ".")
