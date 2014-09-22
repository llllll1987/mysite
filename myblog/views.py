
# Create your views here.

from django.shortcuts import render_to_response,HttpResponse
from myblog.models import Blog,Zhiwei_CMC_Board,CMC_Board,SFPVendor,SFP


def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = []
    # if 'q' in request.GET:
    	q = request.GET['q']
    	if not q:
    		errors.append('Enter a search term')
    	# elif len(q>5):
    		# errors.append('Please enter at most 5 characters')
    	else:
	       	boards = Blog.objects.filter(caption=q)
	       	return render_to_response('search_results.html',
	            {'boards': boards, 'query': q})
		return render_to_response('search_form.html', {'errors': errors})

def zhiwei_board_list(request):
    cmc_boards = Zhiwei_CMC_Board.objects.all()
    return render_to_response("zhiwei_board_list.html", {"cmc_boards": cmc_boards})


def board_tracking(request):
    cmc_boards = CMC_Board.objects.all()
    return render_to_response("board_tracking.html", {"cmc_boards": cmc_boards})

def sfp_tracking(request):
    sfps = SFP.objects.all()
    sfpvendors = SFPVendor.objects.all()
    sfpcount = {"total":sfps.count()}
    temp = sfps.filter(sfp_owner_id = 1)
    sfpcount["in_store"] = temp.count()
    temp = sfps.exclude(sfp_owner_id = 1)
    sfpcount["in_crossteam"] = temp.count()
    # sfpcount_total = sfps.count()
    # sfpcount_in_store = "10"
    # sfpcount_in_crossteam = "20"
    # sfpcount = [sfpcount_total,sfpcount_in_store,sfpcount_in_crossteam]
    return render_to_response("sfp_tracking.html", {"sfps": sfps, "sfpvendors": sfpvendors, "sfpcount":sfpcount})

