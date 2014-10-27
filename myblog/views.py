
# Create your views here.

from django.shortcuts import render_to_response,HttpResponse
from myblog.models import Blog,Author,Zhiwei_CMC_Board,CMC_Board,SFPVendor,SFP,Record_log


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
    records = Record_log.objects.order_by('-log_date')[:6]
    sfpcount = {"total":sfps.count()}
    temp = sfps.filter(sfp_owner_id = 1)
    sfpcount["in_store"] = temp.count()
    temp = sfps.exclude(sfp_owner_id = 1)
    sfpcount["in_crossteam"] = temp.count()
    return render_to_response("sfp_tracking.html", {"sfps": sfps, "sfpvendors": sfpvendors, "sfpcount":sfpcount,"records":records})


def bulk_change_sfp_owner(request):
    input_string = 'FNS18340YE3 AGM183500EC EAK2000994 EAK2000984 SPC183502ZD FNS183815X3 SPC18330307 SPC18330306 NSZ18340310 NSZ18110814 E4T2006908 EA22009544'
    sfp_sn_list = input_string.split()

    sfp_all = SFP.objects.all()
    owner_all = Author.objects.all()
    newsfp_owner = owner_all.get(name = 'xinxwu')
    change_count = 0

    for temp_sfp_sn in sfp_sn_list:
        temp_sfp = sfp_all.get(sfp_sn= temp_sfp_sn)
        temp_sfp.sfp_owner = newsfp_owner
        temp_sfp.save()
        change_count = change_count + 1
    html = "<html><body>Totally %s Models changed success! </body></html>" % change_count
    return HttpResponse(html)

