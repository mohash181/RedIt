from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model




class Post(models.Model):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, primary_key=True)
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
    


    def __str__(self):
        if len(self.title) >= 21 :
            return f"{self.title[:20]}.. By {self.user} on {self.date_created}"
        else:
            return f"{self.title} By {self.user} on {self.date_created}"
    

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

    def get_votes(self):
        return self.votes.difference

#----------------------------


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    animage = models.ImageField()

    def __str__(self):
        return f"An image in {self.post.title}"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    


class Files(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    afile = models.FileField()

    def __str__(self):
        return f"A file in {self.post.title}"

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

class Videos(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    vid = models.FileField()

    def __str__(self):
        return f"A video in {self.post.title}"

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

class Votes(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    downvoted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    upvoted_by = models.ForeignKey(self.post.user, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.difference} votes on {self.post}"

    def apply_difference(self):
        self.difference = self.upvotes + self.downvotes
        return self.difference

    class Meta:
        verbose_name = "Votes"
        verbose_name_plural = "Votes"








# class Comment(models.Model):

#     head = models.on















# Create your models here.





