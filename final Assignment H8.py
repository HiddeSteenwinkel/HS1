def inlezen_beginstation(stations):
    invoer_beginstation = input('Wat is je beginstation: ')
    combi = False
    for station in stations:
        if invoer_beginstation == station:
            combi = True
            break

    if combi:
        return invoer_beginstation
    else:
        inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    invoer_eindstation = input('Wat is je eindstation: ')
    combi = False
    for station in stations:
        if invoer_eindstation == station and stations.index(invoer_eindstation) > stations.index(beginstation):
            combi = True
            break

    if combi:
        return invoer_eindstation
    else:
        inlezen_beginstation(stations)
        print('Deze trein rijdt niet richting de aangegeven kant')

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation is ', beginstation, ' is het', stations.index(beginstation), ' station in het traject' )
    print('Het eindstation is ', eindstation, ' is het', stations.index(eindstation), ' station in het traject')
    print('De afstand in stations is ', (stations.index(eindstation) - stations.index(beginstation)), ' stations')
    print('De prijs is ', (stations.index(eindstation) - stations.index(beginstation)) * 5)
    print('Jij stapt in bij', beginstation, )
    start = stations.index(beginstation)
    while start < stations.index(eindstation):
        print("- ", stations[start])
        start += 1
    print("Jij stapt uit in: ", eindstation)



stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandan', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '`s hertogenbosch', 'Eindhoven', 'Weert', 'Roermond','Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

