from conftest import ModelTestBase, post_to_db, pytest
from models.users import *


class TestingFramework(ModelTestBase):

    def test_framework_produces_virgin_db_and_functions(self):
        users = User(email='email', first_name='luis', last_name='d', phone='7142228402', photo='no photo')
        post_to_db(users, self.db)

        users = User.query.all()

        assert len(users) == 1
        assert users[0].email == 'email'


    def test_framework_produces_virgin_db(self):
        users = User.query.all()

        assert len(users) == 0
        assert users == []


    def test_framework_enforce_relationships_part1(self):
        user_config = UserConfig(1, 'admin privledges', 'vale items')

        with pytest.raises(Exception) as IntegrityError:
            post_to_db(user_config, self.db)

        assert IntegrityError.typename == 'IntegrityError'
        assert 'FOREIGN KEY constraint failed' in str(IntegrityError.__repr__)


    def test_framework_enforce_relationships_part2(self):
        user = User(email='email@gmail.com', first_name='prince', last_name='sky', phone='111-222-4444', photo='no photo')
        post_to_db(user, self.db)
        user = User.query.all()

        assert len(user) == 1
        assert user[0].configuration == None

        user_config = UserConfig(483729875, 'admin privledges', 'vale items')

        with pytest.raises(Exception) as IntegrityError:
            post_to_db(user_config, self.db)

        assert IntegrityError.typename == 'IntegrityError'
        assert 'FOREIGN KEY constraint failed' in str(IntegrityError.__repr__)
