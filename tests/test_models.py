import unittest
from app.models import User, Blog,Comment, Quote
from datetime import datetime



class UserModelTest(unittest.TestCase):


    
    def setUp(self):
        '''
        Test to run before any other tests
        '''
        self.new_user = User(email = 'one@one.com',
                              username = 'gabi',
                              password = 'cat') 
        
            
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(password = 'cat')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
        
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('cat'))
        
    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
        
        

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the blog bost class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1,
                            1,
                             'Python Must Be Crazy',
                             '2019-04-25 08:26:19.580874',
                             'Cryptography',
                             'Great subject')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
        
        
class CommentTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(comments = 'That is a great blog post', post_id = 4456 , posted = '04/12/2019',user_id = 4)

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.body,'One great post')
        self.assertEquals(self.new_comment.timestamp,'2019-04-25 08:26:19.580874')
        self.assertEquals(self.new_comment.user_id,4)
        self.assertEquals(self.new_comment.blog_id,1)

    def test_save_review(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(4456)
        self.assertTrue(len(got_comments) == 1)


class QuoteTest(self):


if __name__ == '__main__':
    unittest.main()