from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),  # Lists all leads
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('create/', views.create_lead, name='create_lead'),  # Form for creating a new lead
    path('edit/<int:lead_id>/', views.edit_lead, name='edit_lead'),  # Edit an existing lead
    path('delete/<int:lead_id>/', views.delete_lead, name='delete_lead'),  # Delete a lead
    path('lead_detail/<int:lead_id>/', views.lead_detail, name='lead_detail'),  # Details for a specific lead

    # Interactions for a specific lead
    path('<int:lead_id>/interactions/', include([
        path('', views.interaction_list, name='interaction_list'),  # List interactions for a lead
        path('create/', views.create_interaction, name='create_interaction'),  # Create a new interaction
        path('edit/<int:interaction_id>/', views.edit_interaction, name='edit_interaction'),  # Edit interaction
        path('interaction/<int:interaction_id>/reply/', views.interaction_detail, name='interaction_detail'),
    ])),

    # Tasks for a specific lead
    path('<int:lead_id>/tasks/', include([
        path('', views.task_list, name='task_list'),  # List tasks for a lead
        path('create_task/', views.create_task, name='create_task'),
        # Create a new task
        path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit task
        path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
    ])),
]
