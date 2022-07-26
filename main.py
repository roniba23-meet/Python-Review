#function to create a youtuve video dictionary
def create_youtube_video(title1, description1, list_hashtag):
    video={ 'title':title1, 'description':description1, 'likes':0, 'dislikes':0, 'comments':{}, 'hashtag':list_hashtag}
    return video
    
    
#function to add a like   
def like(youtube_video):
    if "likes" in youtube_video:
        youtube_video['likes']=youtube_video['likes']+1
    return youtube_video
    
    
#function to add a dislike   
def dislike(youtube_video):
    if "dislikes" in youtube_video:
        youtube_video['dislikes']=youtube_video['dislikes']+1
    return youtube_video
    
    
#function to add a comment
def add_comment(youtubevideo, username, comment_text):
    youtubevideo['comments'][username]=comment_text
    return youtubevideo
    
    
  #function to return precent of similarity between two videos
def similarity_to_videos(video1, video2):
    #sum= variable to count number of similiar hashtags
    sum=0
    #checking for each value in one list, if exist in the other
    for i in range (0,5):
        if video1['hashtag'][i] in video2['hashtag']:
            sum=sum+1
    return sum*20

#testing the first task
test= create_youtube_video("This Is Bad", "I am addicted to Stranger Things", ["5",'6','7', '7'])
print (test)
test= like(test)
test= dislike(test)
test= add_comment(test, "roni", "agree")
print(test)
#testing the second task
test1= create_youtube_video("one", "one", ["a", "b", "c", "d", "e"])
test2= create_youtube_video("two", "two", ["a", "m", "y", "d", "e"])
print("similiarity of precents for '"+test1['title']+"' and '"+test2["title"]+"' is: "+str(similarity_to_videos(test1, test2))+"%")
