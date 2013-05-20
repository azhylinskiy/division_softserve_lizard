#!/usr/bin/env python
def selectall():
    return """
    SELECT role_name as 'Role', id_user as 'Num', user_first_name as 'Firs Name', user_last_name as 'Last Name', user_login as 'Login', user_tel as 'Fone'
    FROM tbl_users INNER JOIN tbl_roles ON tbl_users.user_role = tbl_roles.id_role
    """

def search(pattern):
    search = """
    SELECT role_name as 'Role', id_user as 'Num', user_first_name as 'Firs Name', user_last_name as 'Last Name', user_login as 'Login', user_tel as 'Fone'
    FROM tbl_users INNER JOIN tbl_roles ON tbl_users.user_role = tbl_roles.id_role
    WHERE role_name like '%s' OR user_first_name like '%s' OR user_last_name like '%s' OR user_login like '%s' OR user_tel like '%s'
    """
    pattern = '%'+pattern+'%'
    return search % ((pattern,) * 5)

def insert(fn, ln, lg, pw, r, tel):
    q_role = "select id_role from tbl_roles where role_name = '%s'" % r
    return """
        INSERT INTO `tbl_users`(`user_first_name`, `user_last_name`, `user_login`, `user_password`, `user_role`, `user_tel`)
        VALUES ('%s', '%s', '%s', '%s', (%s), '%s')
        """ % (fn, ln, lg, pw, q_role, tel)

def delete(i):
    del_i = """
    DELETE FROM `tbl_users`
    WHERE id_user = %s
    """
    return del_i % i
