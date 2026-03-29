from collections import defaultdict
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BillRecord
from .forms import BillRecordForm


def index(request):
    records = BillRecord.objects.all()[:20]
    return render(request, 'records/index.html', {'records': records})


def search_records(request):
    query = request.GET.get('q', '').strip()
    grouped_results = defaultdict(list)
    total_count = 0

    if query:
        if query.isdigit():
            bill_no = int(query)
            records = BillRecord.objects.filter(start_no__lte=bill_no, end_no__gte=bill_no)
        else:
            records = BillRecord.objects.filter(customer_name__icontains=query)

        total_count = records.count()
        for r in records:
            grouped_results[r.bill_type].append(r)

    return render(request, 'records/search_results.html', {
        'results': dict(grouped_results),
        'query': query,
        'total_count': total_count
    })


def add_record(request):
    if request.method == "POST":
        form = BillRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BillRecordForm()

    return render(request, 'records/add_record.html', {'form': form})


def record_detail(request, pk):
    record = BillRecord.objects.get(id=pk)
    return render(request, 'records/detail.html', {'record': record})


def edit_record(request, pk):
    record = BillRecord.objects.get(id=pk)

    if request.method == "POST":
        form = BillRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BillRecordForm(instance=record)

    return render(request, 'records/add_record.html', {'form': form})


def delete_record(request, pk):
    record = BillRecord.objects.get(id=pk)
    record.delete()
    return redirect('index')