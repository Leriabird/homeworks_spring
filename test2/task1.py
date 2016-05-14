import sqlite3 as sq

with sq.connect('/Users/Leria/Downloads/data-2.sqlite') as data:
    cur = data.cursor() #create cursor for making queries

#---------1 +
    for row in cur.execute('select * from Users '
                           'order by username'):
       print(row)
#---------2 +
    for row in cur.execute('select * from Users '
                           'order by registered desc limit 5 '):
        print(row)
#---------3 +
    for row in cur.execute('select username, song_id, count(*) as selection '
                           'from Listened inner join users on users.id = user_id '
                           'group by user_id order by selection desc limit 5'):
         print(row)
#---------4 +
    for row in cur.execute('select Artists.name, count(*) as s from Artists '
                           'inner join Albums on artist_id = Artists.id '
                            'group by artists.id order by s desc'):
        print(row)
#---------5 +
for row in cur.execute('select Artists.name, count(*) as s from Artists '
                           'inner join Albums on artist_id = Artists.id '
                            'inner join Songs on Albums.id = Songs.album_id '
                            'group by artists.id order by s desc'):
    print(row)
#---------6 +
    for row in cur.execute('select Artists.name, Albums.name, count(*) as s from Artists '
                           'inner join songs on album_id = albums.id '
                            'inner join albums on artists.id = artist_id '
                            'group by albums.name order by s desc'):
        print(row)
#---------7 +
    for row in cur.execute('select Artists.name, Albums.name, total(duration) as s from Artists '
                           'inner join songs on album_id = albums.id '
                            'inner join albums on artists.id = artist_id '
                            'group by albums.name order by s desc'):
        print(row)
#---------8 +
    for row in cur.execute('select Artists.name, Albums.name, total(duration)/count(*) as s from Artists '
                           'inner join songs on album_id = albums.id '
                            'inner join albums on artists.id = artist_id '
                            'group by albums.name order by s desc'):
        print(row)
#---------9 +
    for row in cur.execute('select Artists.name, Albums.name, Songs.name, count(*) as s from Artists '
                           'inner join songs on album_id = albums.id '
                            'inner join albums on artists.id = artist_id '
                           'inner join listened on song_id = songs.id '
                            'group by listened.song_id order by count(*) desc limit 5'):
        print(row)
#---------10 +
    for row in cur.execute('select Albums.release_year, count(*) as s from Artists '
                           'inner join songs on album_id = albums.id '
                            'inner join albums on artists.id = artist_id '
                           'inner join listened on song_id = songs.id '
                            'group by Albums.release_year order by count(*) desc limit 1'):
        print(row)
#---------11 +
    for row in cur.execute('select Artists.name, Albums.name, Songs.name, start_time from Artists '
                           'inner join songs on Albums.id = album_id '
                           'inner join albums on Artists.id = Albums.artist_id '
                           'inner join listened on Songs.id = song_id '
                           'inner join users on Users.id = user_id '
                           'where users.id = 47 '
                           'order by start_time desc limit 20'):
        print(row)