---
layout: simple-page
title: Computer Centres
header: Our Computer Centres
permalink: /computer-centres/
breadcrumb: Services
comment: Update the operating hours in the _config.yml file!
redirect_from:
 - /services/
---

We operate two computer centres within the NUS Kent Ridge Campus, at the Yusof Ishak House and also at Blk AS8.

![Our Computer Centres at YIH and AS8]({{site.baseurl}}/images/services.jpg)

In YIH, we provide a total of 45 PCs in two clusters equipped with internet access, printing and scanning. To date, we are still the sole provider of public scanning services in NUS.

In AS8, we have more than 44 PCs there, with internet access and printing.

## Operating hours
Here is our centre’s operating hours:

{% assign locations = site.locations %}
{% if site.operating-type == "default" or site.operating-type == "exams" or site.operating-type == "holidays" or site.operating-type == "special" %}
{% assign type = site.operating-type %}
{% else %}
{% assign type = "default" %}
{% endif %}
<table>
    <tr>
        <th></th>
        {% for location in locations %}
        <th>{{location.name}}</th>
        {% endfor %}
    </tr>
    <tr>
        <td>Monday - Friday</td>
        {% for location in locations %}
        {% assign hours = site.operating-hours[type][location.shortname]["hours"][0].time %}
        {% if hours %}
        <td>{{hours}}</td>
        {% else %}
        <td>Closed</td>
        {% endif %}
        {% endfor %}
    </tr>
    <tr>
        <td>Saturday</td>
        {% for location in locations %}
        {% assign hours = site.operating-hours[type][location.shortname]["hours"][1].time %}
        {% if hours %}
        <td>{{hours}}</td>
        {% else %}
        <td>Closed</td>
        {% endif %}
        {% endfor %}
    </tr>
    <tr>
        <td>Sunday</td>
        {% for location in locations %}
        {% assign hours = site.operating-hours[type][location.shortname]["hours"][2].time %}
        {% if hours %}
        <td>{{hours}}</td>
        {% else %}
        <td>Closed</td>
        {% endif %}
        {% endfor %}
    </tr>
</table>

## Printing rates
![Printing rates]({{site.baseurl}}/images/rates.jpg)
