< PROJECT ROOT >
   |
   |-- core/                               # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |-- templates/                     # Templates used to render pages
   |         |
   |         |-- includes/                 # HTML chunks and components
   |         |-- layouts/                  # Master pages
   |         |-- accounts/                 # Authentication pages
   |         |
   |      index.html                       # The default page
   |       *.html                          # All other HTML pages
   |
   |-- authentication/                     # Handles auth routes (login and register)
   |    |-- urls.py                        # Define authentication routes  
   |    |-- forms.py                       # Define auth forms  
   |
   |-- app/                                # A simple app that serve HTML files
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |
   |-- customers/                          # Handles the profile edit     <-------- NEW
   |    |-- __init__.py                    # Defines App init             <-------- NEW
   |    |-- admin.py                       # Defines App admin            <-------- NEW
   |    |-- apps.py                        # Defines App apps             <-------- NEW
   |    |-- forms.py                       # Defines App forms            <-------- NEW
   |    |-- models.py                      # Defines App models           <-------- NEW
   |    |-- signals.py                     # Defines App signals          <-------- NEW
   |    |-- tests.py                       # Defines App tests            <-------- NEW
   |    |-- urls.py                        # Defines App routes           <-------- NEW
   |    |-- views.py                       # Defines App views            <-------- NEW
   |
   |-- requirements.txt                    # Development modules - SQLite storage
   |-- .env                                # Inject Configuration via Environment
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
