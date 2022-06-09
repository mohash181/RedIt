from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model




class Post(models.Model):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    published = models.BooleanField(default=False)
    draft = models.BooleanField(default=False, help_text=_("Save a post as a draft"))
    archived = models.BooleanField(default=False, help_text=_("You may archive a post instead of deleting it."))
    was_archived = models.BooleanField(default=False, help_text=_("Post was archived at some point."))
    edited = models.BooleanField(default=False)
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    date_published = models.DateTimeField( blank=True, null=True, verbose_name="Published On")
    date_edited = models.DateTimeField(blank=True, null=True, verbose_name="Edited On")

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    utd_ratio = models.IntegerField(default=0)
    


    def __str__(self):
        if len(self.title) >= 21 :
            return f"{self.title[:20]}.. By {self.user} on {self.date_created}"
        else:
            return f"{self.title} By {self.user} on {self.date_created}"
    


    # ---------- VOTES METHODS ----------
    def sum_votes(self):
        self.downvotes = -abs(self.downvotes)
        self.votes = self.upvotes + self.downvotes
        return self.votes
    # ---------- END VOTES METHODS ----------


    # ---------- DRAFT METHODS ----------
    def save_as_draft(self):
        self.draft = True
        self.save()

    def is_draft(self):
        return True if self.draft else False

    # ---------- END DRAFT METHODS ----------


    # ---------- PUBLISH METHODS ----------
    def publish(self):
        self.date_published = timezone.now
        self.published = True
        self.save()
    
    def is_published(self):
        return True if self.published else False
    
    def get_published(self):
        # For the user's published posts section in their profile
        # which appears to anyone.
        Post.objects.filter(user=self.user, published=True)

    # ---------- END PUBLISH METHODS ----------


    # ---------- ARCHIVE METHODS ----------
    def archive(self):
        self.archived = True
        self.was_archived = True
        self.published = False
        self.save()
    
    def unarchive(self):
        self.archived = False
        self.published = True
        self.save()
    
    def is_archived(self):
        # Checks if the post is archived.
        return True if self.archived else False
    
    def wasit_archived(self):
        # Checks if the post was an archive before. 
        if (self.was_archived == True) and (self.archived == True):
            return "Post is still archived."
        elif (self.was_archived == True) and (self.archived == False):
            return True
    def get_archived(self):
        # For the user's archived posts section in their profile
        # which appears only to them.
        Post.objects.filter(user=self.user, archived=True)
    
    # ---------- END ARCHIVE METHODS ----------


    # ---------- EDIT METHODS ---------
    def edit_post(self):
        # Changes the instance's values that spicifies that
        # it's been edited.
        self.edited = True
        self.date_edited = timezone.now
        self.save()

    def is_edited(self):
        return True if self.edited else False

    # ---------- END EDIT METHODS ----------

    # ---------- CHILD MODELS METHODS ----------
    def get_images(self):
        return self.images.all()

    def get_files(self):
        return self.files.all()
    
    def get_videos(self):
        return self.videos.all()

    def get_votes(self):
        return self.votes
    # ---------- END CHILD MODELS METHODS ----------

#----------------------------


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="itsimages")
    animage = models.ImageField(blank=True, null=True, upload_to="posts_images/")

    def __str__(self):
        return f"An image on {self.post.title}"



  
    


class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="itsfiles")
    afile = models.FileField(blank=True, null=True, upload_to="posts_files/")

    def __str__(self):
        return f"A file on {self.post.title}"

    

class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="itsvideos")
    vid = models.FileField(blank=True, null=True, upload_to="posts_vids")

    def __str__(self):
        return f"A video on {self.post.title}"

    




class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="itscomments")
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE, related_name="theircomments")
    text = models.TextField(blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)    


    def __str__(self):
        return f"Comment By {self.user} on {self.post.title}"


    # ---------- EDIT METHODS ---------
    def edit_comment(self):
        # Changes the instance's values that spicifies that
        # it's been edited.
        self.edited = True
        self.save()

    def is_edited(self):
        return True if self.edited else False

    # ---------- END EDIT METHODS ----------










# Create your models here.





