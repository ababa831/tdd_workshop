from closed_range import ClosedRange


def initialize(a, b):
    cr = ClosedRange(a, b)
    return cr


cr_default = initialize(3, 8)


class TestClosedRange(object):
    def test_数字以外が入力されたらValueErrorを返す(self):
        try:
            cr = ClosedRange('a', 'b')
        except ValueError:
            cr = None
        assert cr is None

    def test_数字が文字列型として渡された場合は許容する(self):
        cr = ClosedRange('3', '8')
        assert cr.closed_range == [3, 8]

    def test_閉区間を文字列で返す(self):
        """
        stringの'[3, 8]'が帰ってくる
        """
        assert cr_default.return_string() == '[3, 8]'

    def test_aがbより小さい場合はリスト型オブジェクトを返す(self):
        assert cr_default.closed_range == [3, 8]

    def test_aがbと同じ場合はリスト型オブジェクトを返す(self):
        try:
            cr = initialize(1, 1)
        except ValueError:
            cr = None
        assert cr.closed_range == [1, 1]

    def test_aがbより大きい場合はValueErrorとなる(self):
        """
        a > b なa, b を渡すと Error が raise される
        """
        try:
            cr = initialize(2, 1)
        except ValueError:
            cr = None
        assert cr is None

    def test_引数が閉区間の範囲内ならTrueを返す(self):
        input_list = [3, 8]
        actual = [cr_default.is_contained(num) for num in input_list]
        assert actual == [True] * 2

    def test_引数が閉区間の範囲外ならFalseを返す(self):
        input_list = [2, 9]
        actual = [cr_default.is_contained(num) for num in input_list]
        assert actual == [False] * 2

    def test_引数の閉区間があらかじめ設定した閉区間と完全一致するならTrueを返す(self):
        arg = [3, 8]
        assert cr_default.arg_is_equal_to_closed_range(arg)

    def test_引数の閉区間があらかじめ設定した閉区間と完全一致しなければFalseを返す(self):
        arg = [3, 9]
        assert not cr_default.arg_is_equal_to_closed_range(arg)

    def test_arg_is_equal_to_closed_rangeで引数の閉区間が全ての集合値を含むリストである場合でもTrue(self):
        arg = list(range(3, 9))
        assert cr_default.arg_is_equal_to_closed_range(arg)

    def test_引数の閉区間があらかじめ設定した閉区間に完全に含まれるときTrueを返す(self):
        input_list = [[3, 5], [4, 8]]
        actual = [cr_default.arg_is_fully_contained(arg) for arg in input_list]
        assert actual == [True] * 2

    def test_引数の閉区間があらかじめ設定した閉区間に完全に含まれないときFalseを返す(self):
        input_list = [[2, 8], [3, 9]]
        actual = [cr_default.arg_is_fully_contained(arg) for arg in input_list]
        assert actual == [False] * 2

    def test_arg_is_fully_containedで引数の閉区間が全ての集合値を含むリストである場合でもTrue(self):
        arg = list(range(3, 8))
        assert cr_default.arg_is_fully_contained(arg)
