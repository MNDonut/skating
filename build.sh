set -o errexit

python -m venv env
source env/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_superadmin
