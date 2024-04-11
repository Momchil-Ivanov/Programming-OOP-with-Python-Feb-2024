from unittest import TestCase, main

from project.social_media import SocialMedia

if __name__ == '__main__':
    main()

class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia('test', 'YouTube', 1000, "comedy")

        self.social_media_with_posts = SocialMedia('test', 'YouTube', 1000, "comedy")
        post = {'content': "ini", 'likes': 0, 'comments': []}
        self.social_media_with_posts._posts = [post]

        self.social_media_with_posts_lot_of_likes = SocialMedia('test', 'YouTube', 1000, "comedy")
        post = {'content': "ini", 'likes': 100, 'comments': []}
        self.social_media_with_posts_lot_of_likes._posts = [post]

    def test_init(self):

        self.assertEqual(self.social_media._username, 'test')
        self.assertEqual(self.social_media._platform, 'YouTube')
        self.assertEqual(self.social_media._followers, 1000)
        self.assertEqual(self.social_media._content_type, 'comedy')
        self.assertEqual(self.social_media._posts, [])

    def test_followers_are_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.social_media.followers = -1000
        self.assertEqual(str(ex.exception), "Followers cannot be negative.")

    def test_validate_and_set_platform_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.social_media.platform = "Nope"
        self.assertEqual(str(ex.exception), "Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_create_post(self):
        post = {'content': "ini", 'likes': 0, 'comments': []}
        post_content = "testaru_content"
        new_post = {'content': "testaru_content", 'likes': 0, 'comments': []}
        result = self.social_media_with_posts.create_post(post_content)
        expected = f"New comedy post created by test on YouTube."
        self.assertEqual(result, expected)
        self.assertEqual(self.social_media_with_posts._posts, [post, new_post])

    def test_invalid_post_index_negative_or_too_much(self):
        post_idx = -1
        result = self.social_media_with_posts.like_post(post_idx)
        expected = "Invalid post index."
        self.assertEqual(result, expected)

        post_idx = 10
        result = self.social_media_with_posts.like_post(post_idx)
        expected = "Invalid post index."
        self.assertEqual(result, expected)

    def test_like_post_if_below_ten_likes(self):
        post_idx = 0
        result = self.social_media_with_posts.like_post(post_idx)
        expected = f"Post liked by test."
        self.assertEqual(result, expected)
        self.assertEqual(self.social_media_with_posts._posts[0]['likes'], 1)

    def test_like_post_if_above_ten_likes(self):
        post_idx = 0
        result = self.social_media_with_posts_lot_of_likes.like_post(post_idx)
        expected = f"Post has reached the maximum number of likes."
        self.assertEqual(result, expected)
        self.assertEqual(self.social_media_with_posts_lot_of_likes._posts[0]['likes'], 100)

    def test_comment_on_post_below_ten_chars_invalid(self):
        post_idx = 0
        comment = "123"
        result = self.social_media_with_posts.comment_on_post(post_idx, comment)
        expected = f"Comment should be more than 10 characters."

        self.assertEqual(result, expected)
        self.assertEqual(self.social_media_with_posts._posts[0]['comments'], [])

    def test_comment_on_post_above_ten_chars_valid(self):
        post_idx = 0
        comment = "12345678910"
        result = self.social_media_with_posts.comment_on_post(post_idx, comment)
        expected = f"Comment added by test on the post."
        self.assertEqual(result, expected)
        self.assertEqual(self.social_media_with_posts._posts[0], {'comments': [{'comment': '12345678910', 'user': 'test'}],
 'content': 'ini',
 'likes': 0})
