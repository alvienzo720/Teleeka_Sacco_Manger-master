from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .forms import  CreateClientForm, CreateDepositForm, CreateWithdrawlForm , LoginForm, SignUpForm, createLoanForm
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
from .decorators import unauthnticated_user
# from django.contrib.auth.models import Group
from .models import *

# login View
def loginPage(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "teleeka/login.html", {"form": form, "msg" : msg})

# register view
def reigsterPage(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "teleeka/register.html", {"form": form, "msg" : msg, "success" : success })



# home view
@login_required(login_url='login')
def home(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	loans = Loan.objects.all()
	loan_count = loans.count()
	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount

	context = {'clients':clients,'client_count':client_count,'deposits':deposits,
				'count_deposit':count_deposit,'loans':loans, 'loan_count':loan_count,
				'all_time_contributions':all_time_contributions}

	return render(request, 'teleeka/index.html', context)


# Logout View
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')


# Profile View
def profile(request,pk):
	client = Client.objects.get(id=pk)
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	loans = Loan.objects.all()
	loan_count = loans.count()

	depo = client.deposit_set.all()

	loans = client.loan_set.all()

	total_personal_contributions = 0

	all_time_contributions = 0

	count_personal_contributions = depo.count()

	for obj in depo:
		total_personal_contributions += obj.amount


	total_personal_loan = 0

	for obj in loans:
		total_personal_loan += obj.amount


	for deposit in deposits:
		all_time_contributions += deposit.amount


	context = {'depo':depo, 'client':client,'deposits':deposits,
				'count_deposit':count_deposit, 'loans':loans, 
				'total_personal_contributions':total_personal_contributions,
				'total_personal_loan':total_personal_loan,
				'count_personal_contributions':count_personal_contributions,
				'clients':clients, 'client_count':client_count,'loans':loans, 'loan_count':loan_count,
				'all_time_contributions':all_time_contributions}


	return render(request, 'teleeka/profile.html',context)

# deposit view
def deposit(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	loans = Loan.objects.all()
	loan_count = loans.count()
	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount

	context = {'clients':clients,'client_count':client_count,'deposits':deposits,
				'count_deposit':count_deposit,'loans':loans, 'loan_count':loan_count,
				'all_time_contributions':all_time_contributions}
	

	return render(request, 'teleeka/deposit.html', context)

# withdrawl view
def withdrawl(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	loans = Loan.objects.all()
	loan_count = loans.count()
	all_time_contributions = 0
	total_loans_given = 0

	for loan in loans:
		total_loans_given += loan.amount

	for deposit in deposits:
		all_time_contributions += deposit.amount


	context = {'all_time_contributions':all_time_contributions,'loans':loans,'loan_count':loan_count,
				'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'total_loans_given':total_loans_given}

	return render(request, 'teleeka/withdrawl.html', context)


# tansaction view
def transactions(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	loans = Loan.objects.all()
	loan_count = loans.count()

	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount


	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'all_time_contributions':all_time_contributions,
				'loans':loans, 'loan_count':loan_count}
	
	return render(request, 'teleeka/transactions.html', context)


# clients view
def clientPage(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	loans = Loan.objects.all()
	loan_count = loans.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount
	
	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'all_time_contributions':all_time_contributions, 'loan_count':loan_count}

	return render(request, 'teleeka/clientspage.html', context)


#create Client View
def createClient(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	loans = Loan.objects.all()
	loan_count = loans.count()
	count_withdrawls = withdrawls.count()
	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount

	if request.method == 'POST':
		form = CreateClientForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('clientpage')
			except:
				pass
	else:
		form = CreateClientForm()
	
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'all_time_contributions':all_time_contributions,'loan_count':loan_count}


	return render(request, 'teleeka/createClient.html',context)
					

#edit Client View

def editClient(request, pk):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	client = Client.objects.get(id=pk)
	formset = CreateClientForm(instance=client)
	if request.POST == 'POST':
		print("Printing POST: ", request.POST)
		formset = CreateClientForm(request.POST, instance=client)
		if formset.is_valid():
			formset.save()
				# model = formset.instance
			return redirect('clientpage')
			# except Exception as e:
			# 	pass
	context = {'formset':formset,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls}
	return render(request, 'teleeka/editClient.html', context)



# delete Client View
def deleteClient(request,pk):
	client = Client.objects.get(id=pk)
	if request.method == 'POST':
		client.delete()
		return redirect('clientpage')
	context = {'client':client}
	return render(request, 'teleeka/delteClient.html', context)

# create Deposit View
def createDeposit(request):

	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	loans = Loan.objects.all()
	loan_count = loans.count()
	all_time_contributions = 0
	for deposit in deposits:
		all_time_contributions += deposit.amount

	if request.method == 'POST':
		form = CreateDepositForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('deposit')
			except:
				pass
	else:
		form = CreateDepositForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls,
				'loans':loans, 'loan_count':loan_count,'all_time_contributions':all_time_contributions}


	
	return render(request, 'teleeka/createDeposit.html', context)

# delete Deposit view
def deleteDeposit(request,pk):
	deposit = Deposit.objects.get(id=pk)
	if request.method == 'POST':
		deposit.delete()
		return redirect('deposit')
	context = {'deposit':deposit}
	return render(request, 'teleeka/deleteDeposit.html', context)


# create withdrawl view
def CreateLoan(request):
	loans = Loan.objects.all()
	loan_count = loans.count()
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()

	if request.method == 'POST':
		form = createLoanForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('withdrawl')
			except:
				pass
	else:
		form = createLoanForm()
	
	context = {'loans':loans,'loan_count':loan_count,'form':form,'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls}


	return render(request, 'teleeka/createWithdraw.html', context)


# delete withdrawl view
def deleteLoan(request,pk):
	loan = Loan.objects.get(id=pk)
	if request.method == 'POST':
		loan.delete()
		return redirect('withdrawl')
	context = {'loan':loan}
	return render(request, 'teleeka/deleteWithdrawl.html', context)


# group page view
def groupPage(request):
	deposits = Deposit.objects.all()
	count_deposit = deposits.count()
	clients = Client.objects.all()
	client_count = clients.count()
	withdrawls = Withdrawl.objects.all()
	count_withdrawls = withdrawls.count()
	context = {'clients':clients, 'client_count':client_count, 'deposits':deposits,
				'count_deposit':count_deposit, 'withdrawls':withdrawls,'count_withdrawls':count_withdrawls}

	return render(request, 'teleeka/groupPage.html', context)




