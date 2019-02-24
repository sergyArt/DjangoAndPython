const renderProduct = ({id, name, image}) => (
    `
    <div class="toy">
		<div class="photo2">
			<p><a href="/catalog/${ id }/"><img src="${ image ? image : '/media/ded.png' }" alt="${ name }" width="150" heigth="150" hspace="4" vspace="4"></a></p>
		</div>
		<div class="linkproduct2">
			<a href="/catalog/${ id }/">${ name }</a>
			<a href=""></a>
		</div>
	</div>

	`
)