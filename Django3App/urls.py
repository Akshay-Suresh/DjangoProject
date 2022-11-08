from django.urls import path

from Django3App import views, adminViews, studentViews, ParentViews

urlpatterns = [
    #views
    path('', views.home, name='home'),
    path('reg', views.reg_view, name='reg'),
    path('Login_View', views.Login_View, name='Login_View'),

    #adminViews
    path('admin_view', adminViews.admin_view, name='admin_view'),
    path('View_Student', adminViews.View_Student, name='View_Student'),
    path('Delete_Student/<int:id>/', adminViews.Delete_Student, name='Delete_Student'),
    path('View_Parent', adminViews.View_Parent, name="View_Parent"),
    path('Addfood', adminViews.AddFood, name='Addfood'),
    path('Viewfood',adminViews.ViewFood, name='Viewfood'),
    path('Deletefood/<int:id>', adminViews.DeleteFood, name='Deletefood'),
    path('Room_Add', adminViews.Room_Add, name='Room_Add'),
    path('Room_View', adminViews.Room_View, name='Room_View'),
    path('AddAttendance', adminViews.AddAttendance, name='AddAttendance'),
    path('mark/<int:id>', adminViews.mark, name='mark'),
    path('ViewAttendancePresent', adminViews.ViewAttendancePresent, name='ViewAttendancePresent'),
    path('ViewAttendanceAbsent', adminViews.ViewAttendanceAbsent, name='ViewAttendanceAbsent'),
    path('view_attendance', adminViews.view_attendance, name='view_attendance'),
    path('day_attendance/<date>/', adminViews.day_attendance, name='day_attendance'),
    path('Alot_Room', adminViews.AlotRoom_View, name='Alot_Room'),
    path('View_Alot_Room', adminViews.ViewAlotRoom, name='View_Alot_Room'),

    #studentViews
    path('student_view', studentViews.student_view, name='student_view'),
    path('Student_Reg_View', studentViews.Student_Reg_View, name='Student_Reg_View'),
    path('StudentAttendanceView', studentViews.StudentAttendanceView, name='StudentAttendanceView'),
    path('StudentFoodView', studentViews.StudentFoodView, name='StudentFoodView'),

    #ParentViews
    path('Parent_Reg_View', ParentViews.Parent_Reg_View, name='Parent_Reg_View'),
    path('parent_view', ParentViews.parent_view, name='parent_view'),
    path('StudentAttendanceView_Parent', ParentViews.StudentAttendanceView_Parent, name='StudentAttendanceView_Parent'),
    # path('RegParentView', ParentViews.RegParentView, name='RegParentView'),
    # path('RegParent', ParentViews.RegParent, name='RegParent'),
    # path('ParentReg', ParentViews.ParentReg, name='ParentReg')
]