#!/usr/bin/env bash

drop() {
    rm passes/migrations/0*.py
    echo "Removed migrations"
    echo "DROP TABLE passes_address CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_pass CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_person CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_applicationstatus CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_area CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_biometrics CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_disctype CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_organisation CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_orgtype CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_pass_pass_privileges CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_passprivilege CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_passstatus CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_role CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_site CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_sitetype CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_telecoms CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_vetting CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE passes_proofidtype CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE django_content_type CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE django_admin_log CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE django_migrations CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE django_session CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_group CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_group_permissions CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_permission CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_user CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_user_groups CASCADE;" | ./manage.py dbshell
    echo "DROP TABLE auth_user_user_permissions CASCADE;" | ./manage.py dbshell
    echo "Tables dropped."
    echo
}
drop
