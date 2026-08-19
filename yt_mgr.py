import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
# videos are dumped at file(written in files)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start = 1):  
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
        print("\n")
        print("*"*70)

# enumerate will add indexing , start =1 will help to start indexing from 1


def add_video(videos):
    name = input("enter video name")
    time = input("enter video time")
    videos.append({'name' : name, 'time' : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("enter the new video name ")
        time = input("enter the new video time ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter video no to be deleted"))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)

    else:
        print("invalid index")

def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all yt videos")
        print("2. Add a yt video")
        print("3. Update a yt video detail")
        print("4. Delete a yt video")
        print("5. Exit the app")
        choice = input("enter ur choice :")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case '6':
                print("invalid choice")

if __name__ == "__main__":
    main()

