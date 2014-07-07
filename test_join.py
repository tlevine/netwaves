import nose.tools as n

from join import new_image_size

def test_new_image_size():
    n.assert_tuple_equal(new_image_size(100, (100, 100), 1), (10, 10))
    n.assert_tuple_equal(new_image_size(400, (100, 400), 1), (10, 40))
    n.assert_tuple_equal(new_image_size(400, (100, 400), 2), (5, 20))
    n.assert_tuple_equal(new_image_size(399, (100, 400), 2), (5, 20))
