<div class="has-text-centered">

<h2>We found some bias</h2>

{% if template_sentiments.get('Anger', False) %}
        <span class="icon is-large {% if template_sentiments.get('Anger', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Anger: {{ template_sentiments.get('Anger', 0.0) *100 | int}} %">
            <i class="fas fa-3x fa-angry"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Fear', False) %}
        <span class="icon is-large {% if template_sentiments.get('Fear', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Fear: {{ template_sentiments.get('Fear', 0.0) *100 | int}} %">
            <i class="fas fa-3x fa-ghost"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Joy', False) %}
        <span class="icon is-large {% if template_sentiments.get('Joy', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Joy: {{ template_sentiments.get('Joy', 0.0) *100 | int}} %">
            <i class="fas fa-3x fa-smile"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Sadness', False) %}
        <span class="icon is-large {% if template_sentiments.get('Sadness', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Sadness: {{ template_sentiments.get('Sadness', 0.0) *100 | int}} %">
            <i class="fas fa-3x fa-sad-tear"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Analytical', False) %}
        <span class="icon is-large {% if template_sentiments.get('Analytical', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Analytical: {{ template_sentiments.get('Analytical', 0.0) *100 | int}} %">
            <i class="fas fa-3x fa-diagnoses"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Confident', False) %}
        <span class="icon is-large {% if template_sentiments.get('Confident', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Confident: {{ template_sentiments.get('Confident', 0.0) * 100 | int}} %">
            <i class="fas fa-3x fa-clipboard-check"></i>
        </span>
{% endif %}

{% if template_sentiments.get('Tentative', False) %}
        <span class="icon is-large {% if template_sentiments.get('Tentative', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Tentative: {{ template_sentiments.get('Tentative', 0.0) * 100 | int }} %">
            <i class="fas fa-3x fa-history"></i>
        </span>
{% endif %}
<hr/>

<h2>Verify with these sources</h2>

{% for item in template_articles %}
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="{{ item['urlToImage']}}">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <a href="{{item['url']}}" target="_blank">
        {{item['title']}}
      </a>
    </div>
  </div>
</article>
{% endfor %}
