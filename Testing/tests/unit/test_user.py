from conftest import ModelTestBase, post_to_db, pytest
from models.users import *


@pytest.mark.usefixtures(
    "user", "user_config", 'role', 'permission', 'role_permission_link'
)
class TestUserModel(ModelTestBase):

    def test_create_user(self):
        post_to_db(self.user, self.db)

        users = User.query.all()

        assert len(users) == 1
        assert str(users[0].__repr__) == '<bound method User.__repr__ of User 1>'
        assert users[0].photo == 'photo.jpeg'
        assert users[0].email == 'test@gmail.com'
        assert users[0].first_name == 'Lucy'
        assert users[0].last_name == 'Ferr'
        assert users[0].phone == '7146668402'
        assert users[0].photo == 'photo.jpeg'
        assert users[0].created_at != None
        assert users[0].updated_at != None
        assert users[0].check_password('some men just want to watch the world burn') == True

        assert users[0].configuration == None
        assert users[0].roles == []


    def test_user_userconfig_relation(self):
        post_to_db(self.user, self.db)

        # Post muliple configurations for same users to test 1 to 1 relation
        post_to_db(self.user_config, self.db)
        post_to_db(self.user_config, self.db)
        post_to_db(self.user_config, self.db)

        user = User.query.filter_by(email='test@gmail.com').first()
        user_config = UserConfig.query.filter_by(user_id=user.id).first()

        assert user.configuration == user_config
        assert user_config.user == user


    def test_user_role_relation(self):
        post_to_db(self.user, self.db)
        post_to_db(self.role, self.db)
        post_to_db(self.permission, self.db)
        post_to_db(self.role_permission_link, self.db)

        user = User.query.filter_by(email='test@gmail.com').first()

        roles = Roles.query.filter().all()

        permissions = Permissions.query.filter().all()

        link = RolesPermissionsLink.query.filter().all()

        assert user.roles == roles
        assert user.roles[0].permission == permissions

        assert roles[0].name == 'supervisor'
        assert roles[0].user_id == user.id
        assert roles[0].user == user
        assert roles[0].permission == permissions

        assert permissions[0].name == 'full admin'
        assert permissions[0].role == roles

        assert link[0].role_id == roles[0].id
        assert link[0].permission_id == permissions[0].id

        assert roles[0].created_at != None
        assert roles[0].updated_at != None

        assert permissions[0].created_at != None
        assert permissions[0].updated_at != None
