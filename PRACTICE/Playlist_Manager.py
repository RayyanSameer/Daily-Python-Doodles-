#Simple Playlist manager built to re-inforce my learning on dictionaries

play_lists = []

while True:
    print("Welcome to playlist manager !")
    print("(1) Create Playlist")
    print("(2) Delete Playlist")
    print("(3) Search Song")
    print("(4) Veiw Playlists")

    choice = input("Enter your choice : ")
    if choice == "1" :
        #add
        no_of_songs = int(input(("How many songs are you adding? : ")))
        count = 0
        for _ in range(no_of_songs):

            song= input("Song : ")
            artist = input("Artist : ")
            genere = input("Genere: ")
            play_lists.append({"song" : song, "artist": artist,"genre":genere})
            count += 1 
            
    elif choice == "2":
        #delete
        target = input("What to remove?")
        found = False
        for music in play_lists:
            if music["song"] == target:
                play_lists.remove(music)
                print("Removed: ",target )
                found = True
                break
        if not found:
            print("Not found :)")

    elif choice == "3":
        #search 
        name = input("Search name: ")
        for music in play_lists:
            if music["song"] == name:
                print("Found:", music)
                break
        else:
            print("Not found.")

    elif choice == '4':
        if play_lists:
            print("\nYour Playlist:")
            for i, music in enumerate(play_lists, start=1):
                print(f"{i}. {music['song']} by {music['artist']} [{music['genre']}]")
        else:
            print("Playlist is empty.")
    elif choice == 5:    
        break
    


                    

    