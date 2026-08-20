
import sqlite3

conn = sqlite3.connect('yt_videos.db')
# Ye yt_videos.db naam ki database file ke saath connection banata hai.
cursor = conn.cursor()
# cursor database ko commands dene ke kaam aata hai.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
# So ye basically bol raha hai videos table ka pura data lao.
    for row in cursor.fetchall():
# SQL query se aayi saari rows return karta hai.
        print(row)
def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
# Database mein jo change kiya hai usko permanently save karta hai.

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()


def delete_videos(video_id):
    cursor.execute("DELETE FROM videos where id = ? ",(video_id,))
    conn.commit()


def main():
    while True:
        print("\n Yt manager app with DB")
        print("1. List Videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. exit app")
        choice = input("enter ur choice")

        if choice =='1':
            list_videos()
        elif choice =='2':
            name = input("enter video name:")
            time = input("enter video time:")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("enter video id to update")
            name = input("enter video name:")
            time = input("enter video time:")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("enter video id to delete:")
            
            delete_videos(video_id)
        elif choice == '5':
            break
        
        else:
            print("invalid choice")
    conn.close()


if __name__ == "__main__":
    main()
