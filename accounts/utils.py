
def detectUser(user):
    if user.role==1:
        redirectUrl = 'vendorDashboard'
        return redirectUrl
    elif user.rol==2:
        redirectUrl = 'userDashboard'
        return redirectUrl
    elif user.role==None and user.is_superadmin:
        redirectUrl='/admin'
        return redirectUrl